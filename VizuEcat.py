import json


def is_key_in_dict(my_dict, key):
    if key in my_dict.keys():
        return True
    else:
        return False


class EcatParser:
    def __init__(self, fileName):
        self.fileName = fileName
        self.sdoDictList = [] # creates an empty list
        self.pdoList = []

    def parse(self):
        with open(self.fileName) as json_file:
            data = json.load(json_file)

            for packet in data:
                if not is_key_in_dict(packet, '_source'):
                    continue
                source = packet['_source']

                if not is_key_in_dict(source, 'layers'):
                    continue
                layers = source['layers']

                if layers['frame']['frame.number'] == "10065":
                    a = "d"

                if not is_key_in_dict(layers, 'ecat'):
                     continue
                ecat_data = layers['ecat']

                for k, ecat_frame in ecat_data.items():
                    if not is_key_in_dict(ecat_frame, 'ecat_mailbox'):
                        continue

                    ecat_mailbox = ecat_frame['ecat_mailbox']

                    if not is_key_in_dict(ecat_mailbox, 'ecat_mailbox.coe_tree'):
                        continue

                    ecat_coe_tree = ecat_mailbox['ecat_mailbox.coe_tree']

                    if not is_key_in_dict(ecat_coe_tree, 'ecat_mailbox.coe.type'):
                        continue
                    else:
                        ecat_coe_type = ecat_coe_tree['ecat_mailbox.coe.type']

                    ecat_coe_type = ecat_coe_type.strip()

                    idx = ""
                    # handle the packet according to CoE Type
                    if ecat_coe_type == "1":
                        idx = "NA"
                        subidx = "NA"
                        sdo_data = ""
                        sdo_type = "EMERGENCY"
                    else:
                        if ecat_coe_type == "2":
                            sdo_type = "SDO Request"
                        elif ecat_coe_type == "3":
                            sdo_type = "SDO Response"

                        if not is_key_in_dict(ecat_coe_tree, 'ecat_mailbox.coe.sdoidx'):
                            continue

                        idx = str(ecat_coe_tree['ecat_mailbox.coe.sdoidx']).replace("0x0000", "0x")
                        subidx = str(ecat_coe_tree['ecat_mailbox.coe.sdosub']).replace("0x000000", "0x")

                        if is_key_in_dict(ecat_coe_tree, 'ecat_mailbox.coe.dsoldata'):
                            sdo_data = ecat_coe_tree['ecat_mailbox.coe.dsoldata']
                        elif is_key_in_dict(ecat_coe_tree, 'ecat_mailbox.coe.sdodata'):
                            sdo_data = ecat_coe_tree['ecat_mailbox.coe.sdodata']
                        else:
                            sdo_data = 'No Data'

                    # if ecat_frame['Header']['ecat.adp'] == '0x000003e9':

                    print('No:' + layers['frame']['frame.number'] + ", Slave Addr: " + ecat_frame['Header'][
                        'ecat.adp'] + ', SDO: ' + idx + ' sub ' + subidx + ' DATA: ' + sdo_data)

                    # Create dictionary with Frame data
                    mailBoxPacket = {}  # create empty dictionary
                    mailBoxPacket['No'] = layers['frame']['frame.number']
                    mailBoxPacket['addr'] = str(ecat_frame['Header']['ecat.adp']).replace("0x0000", "0x")
                    mailBoxPacket['index'] = idx
                    mailBoxPacket['subIndex'] = subidx
                    mailBoxPacket['sdoType'] = sdo_type
                    mailBoxPacket['data'] = sdo_data

                    #  Add dictionary to frame list
                    self.sdoDictList.append(mailBoxPacket)

    def getSdoList(self):
        return self.sdoDictList

    def getPdoList(self):
        return self.pdoList

if __name__ == "__main__":
    parser = EcatParser("trace1.json")
    parser.parse()










