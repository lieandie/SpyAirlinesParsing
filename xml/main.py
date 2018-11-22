from xml.dom.minidom import parse, Document, Element, Text
import csv
import copy

if __name__ == '__main__':
    cell_delimiter = ';'

    input_file = parse('../assets/Pointz.xml')
    print 'XML loaded'

    output_file_user = open('../assets/parsed/PointzAggregator-AirlinesData.xml.user.csv', 'wb')
    output_file_card = open('../assets/parsed/PointzAggregator-AirlinesData.xml.card.csv', 'wb')
    output_file_activity = open('../assets/parsed/PointzAggregator-AirlinesData.xml.activity.csv', 'wb')
    print 'Files created'

    output_file_user_writer = csv.writer(output_file_user, delimiter=cell_delimiter)
    output_file_card_writer = csv.writer(output_file_card, delimiter=cell_delimiter)
    output_file_activity_writer = csv.writer(output_file_activity, delimiter=cell_delimiter)
    print 'Writers created'

    user_header = ['id', 'first_name', 'last_name', 'id_card']
    card_header = ['id', 'id_card_link', 'bonus_program', 'number']
    activity_header = ['id', 'code', 'date', 'departure', 'arrival', 'fare', 'id_card']

    output_file_user_writer.writerow(user_header)
    output_file_card_writer.writerow(card_header)
    output_file_activity_writer.writerow(activity_header)
    print 'Headers written'

    user_current_id = 0
    card_link_current_id = 0
    activity_current_id = 0
    card_current_id = 0

    current_user_node_num = 1

    user_nodes = input_file.getElementsByTagName('user')

    print 'Processing ' + str(len(user_nodes)) + ' user nodes'
    for user_node in user_nodes:
        print str(current_user_node_num) + ' of ' + str(len(user_nodes))
        user_name_node = user_node.getElementsByTagName("name")[0]
        user_row = [user_current_id, user_name_node.getAttribute('first'), user_name_node.getAttribute('last')]
        card_nodes = user_node.getElementsByTagName('card')
        for card_node in card_nodes:
            card_row = [card_current_id, card_link_current_id, card_node.getElementsByTagName('bonusprogramm')[0].childNodes[0].wholeText,
                        card_node.getAttribute('number')]
            activity_nodes = card_node.getElementsByTagName('activity')
            output_file_card_writer.writerow(card_row)
            card_current_id += 1
            for activity_node in activity_nodes:
                if isinstance(activity_node, Element):
                    activity_row = [activity_current_id]
                    activity_childs = activity_node.childNodes
                    for activity_child in activity_childs:
                        if isinstance(activity_child, Element):
                            activity_row.append(activity_child.childNodes[0].wholeText)
                    activity_row.append(card_link_current_id)
                    output_file_activity_writer.writerow(activity_row)
                    activity_current_id += 1
                    activity_row[0] = activity_current_id
        user_row.append(card_link_current_id)
        output_file_user_writer.writerow(user_row)
        user_current_id += 1
        card_link_current_id += 1
        user_row[0] = user_current_id
        current_user_node_num += 1
    output_file_user.close()
    output_file_card.close()
    output_file_activity.close()
