## Synchronization between Position & Priority

I did this by defining a dictionary called fleet_view and attaching it to the Robot Node, this would be the saved data of every other robot in the node, with their robot_ids and keys and RobotStates as values, and whenever a callback of either position/priority topic is triggered, it writes to the individual robot_id key, and changes the RobotState within to the new values.

### RQT Graphs

![Graph 1](https://cdn.discordapp.com/attachments/472433602861465611/1517632346587795586/Screenshot_from_2026-06-19_19-49-24.png?ex=6a37a583&is=6a365403&hm=18f1cac64f8f685e81bcf2fd74c364b706cba641f736ad94d9593a65321c2014&)

![Graph 2](https://cdn.discordapp.com/attachments/472433602861465611/1517632346881392690/Screenshot_from_2026-06-19_19-49-46.png?ex=6a37a583&is=6a365403&hm=a189175f5ab8c0af978957a8c4a2c41a971a24ce3766f1b56bdb13bccc6d98e8&)
