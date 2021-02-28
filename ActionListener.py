import Leap
from datetime import datetime
import csv
import os


class ActionListener(Leap.Listener):
    """
    listener for all events in Leap Motion controller (extends Leap.Listener)

    letter - symbol that we are currently tracking

    creates in folder ./collected_data csv file with all frames collected during to session
    """
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']

    def __init__(self, letter):
        Leap.Listener.__init__(self)
        if not os.path.exists("collected_data"):
            os.mkdir("collected_data")
        self.file = open("./collected_data/" + letter + "_" + datetime.now().strftime("%d-%m_%H-%M-%S") + ".csv", "w")
        self.writer = csv.writer(self.file)
        header = ['hand_type',
                  'position_x', 'position_y', 'position_z',
                  'roll', 'pitch', 'yaw',
                  'arm_dir_x', 'arm_dir_y', 'arm_dir_z',
                  'wrist_pos_x', 'wrist_pos_y', 'wrist_pos_z',
                  'elbow_pos_x', 'elbow_pos_y', 'elbow_pos_z']

        for i in range(5):
            header.extend([self.finger_names[i] + '_finger_id', 'finger_length', 'finger_width'])
            for b in range(0, 4):
                header.extend(['prev_joint_x', 'prev_joint_y', 'prev_joint_z',
                               'next_joint_x', 'next_joint_y', 'next_joint_z',
                               'direction_x', 'direction_y', 'direction_z'])

        self.writer.writerow(header)

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"
        self.file.close()

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
            frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))

        # Get hands
        for hand in frame.hands:

            vector = [-1 if hand.is_left else 1,
                      hand.palm_position[0], hand.palm_position[1], hand.palm_position[2],
                      hand.palm_normal.roll, hand.direction.pitch, hand.direction.yaw,
                      hand.arm.direction[0], hand.arm.direction[1], hand.arm.direction[2],
                      hand.arm.wrist_position[0], hand.arm.wrist_position[1], hand.arm.wrist_position[2],
                      hand.arm.elbow_position[0], hand.arm.elbow_position[1], hand.arm.elbow_position[2]]

            # Get fingers
            for finger in hand.fingers:
                vector.extend([finger.id, finger.length, finger.width])
                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)
                    vector.extend([bone.prev_joint[0], bone.prev_joint[1], bone.prev_joint[2],
                                   bone.next_joint[0], bone.next_joint[1], bone.next_joint[2],
                                   bone.direction[0], bone.direction[1], bone.direction[2]])

            self.writer.writerow(vector)

        if not frame.hands.is_empty:
            print ""
