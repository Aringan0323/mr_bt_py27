#!/usr/bin/env python

import rospy
from interpreter import TreeBuilder
from ros_behavior_tree import ROSBehaviorTree

if __name__ == '__main__':


    rospy.init_node('person_follower')

    tb = TreeBuilder('tree_jsons/test/forward_wall.json')
    root, blackboard = tb.build_tree()
        # tb.draw_tree()
        # root.tick(blackboard)
        # # print(name + ": " + str(root.tick(blackboard)))

    tree = ROSBehaviorTree(root, blackboard)
    rospy.spin()

    
