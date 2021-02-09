import Leap
from datetime import datetime
import csv


class ActionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def __init__(self, letter):
        Leap.Listener.__init__(self)
        self.file = open("./collected_data/" + letter + "_" + datetime.now().strftime("%d-%m_%H-%M-%S") + ".csv", "w")
        self.writer = csv.writer(self.file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

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

            vector = [-1 if hand.is_left else 1, hand.palm_position,
                      hand.palm_normal.roll, hand.direction.pitch,
                      hand.direction.yaw, hand.arm.direction,
                      hand.arm.wrist_position, hand.arm.elbow_position]

            # Get fingers
            for finger in hand.fingers:
                vector.extend([finger.id, finger.length, finger.width])
                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)
                    vector.extend([bone.prev_joint, bone.next_joint, bone.direction])

            self.writer.writerow(vector)

        if not frame.hands.is_empty:
            print ""
