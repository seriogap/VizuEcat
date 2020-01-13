import json


def is_key_in_dict(my_dict, key):
    if key in my_dict.keys():
        return True
    else:
        return False


with open('trace1.json') as json_file:

    data = json.load(json_file)

    for packet in data:

        if not is_key_in_dict(packet,'_source'):
            continue

        source = packet['_source']

        if not is_key_in_dict(source,'layers'):
            continue

        layers = source['layers']

        if not is_key_in_dict(layers,'ecat'):
            continue

        ecat_data = layers['ecat']

        for k, ecat_frame in ecat_data.items():
            if not is_key_in_dict(ecat_frame, 'ecat_mailbox'):
                continue

            ecat_mailbox = ecat_frame['ecat_mailbox']

            if not is_key_in_dict(ecat_mailbox, 'ecat_mailbox.coe_tree'):
                continue

            ecat_coe_tree = ecat_mailbox['ecat_mailbox.coe_tree']

            if not is_key_in_dict(ecat_coe_tree, 'ecat_mailbox.coe.sdoidx'):
                continue

            idx = ecat_coe_tree['ecat_mailbox.coe.sdoidx']
            subidx = ecat_coe_tree['ecat_mailbox.coe.sdosub']

            if is_key_in_dict(ecat_coe_tree, 'ecat_mailbox.coe.dsoldata'):
                sdo_data = ecat_coe_tree['ecat_mailbox.coe.dsoldata']
            elif is_key_in_dict(ecat_coe_tree, 'ecat_mailbox.coe.sdodata'):
                sdo_data = ecat_coe_tree['ecat_mailbox.coe.sdodata']
            else:
                sdo_data = 'No Data'

            if ecat_frame['Header']['ecat.adp'] == '0x000003e9':
                print('No:' + layers['frame']['frame.number'] + ", Slave Addr: " + ecat_frame['Header']['ecat.adp'] + ', SDO: ' + idx + ' sub ' + subidx + ' DATA: ' + sdo_data)






