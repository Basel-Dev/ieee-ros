Nodes are pieces of a modular system meant to serve singular purposes and to communicate with each other in different ways
to deliver/process data and execute functions of a robot, like a Node for a LIDAR Sensor, and a Node for Motor(s)

Topics are essentially a way for Nodes to communicate by establishing a Publisher-Subscriber system, where a type of message/data is
defined to be sent from a Publisher and listened to from a Subscriber, where any node can publish/subscribe to the topic to
serve its purpose

Services are another way for Nodes to communicate, but instead of a Publisher-Subscriber system, its a Server-Client system where
the client would request with a message and the server would take the request message and from it, reply back with a response message

The command to draw the star was with ros2 topic pub.
