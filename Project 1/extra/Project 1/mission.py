# from pathfinding import find_path
# from models.drone import DroneStatus  # هيسترد حالات الدرون


# حساب استهلاك البطارية
def battery_use(steps, weight):
    return steps * (1 + weight * 0.1)


# التحقق من البطارية
# def can_fly(drone, required_battery):
#     return drone.battery >= required_battery


# # تشغيل الرحلة
# def start_trip(drone, package, grid):  # اعملى رحله باستخدام الدرون و الشحنه و الخريطه

#     # هات الطريق من مكان الدرون الحالى الى مكان التسليم
#     path = find_path(drone.position, package.destination, grid)

#     # لو مفيش طريق
#     if not path:
#         print("No path found")
#         return False  # انهاء الداله

#     # عدد الخطوات
#     steps = len(path)

#     # حساب البطارية
#     battery_needed = battery_use(steps, package.weight)

#     # رايح وجاي
#     total_battery = battery_needed * 2

#     # لو البطارية مش كفاية
#     if not can_fly(drone, total_battery):
#         print("Battery not enough")
#         return False

#     # الدرون بدأ يتحرك
#     drone.set_status(DroneStatus.MOVING)

#     # الحركة خطوة خطوة
#     for step in path:
#         drone.position = step
#         drone.consume_battery(1 + package.weight * 0.1)  # كل خطوه تقلل البطاريه

#         print(f"Drone moving to {step} | Battery: {drone.battery:.1f}%")

#         if drone.battery <= 10:
#             print("Low battery! Going home...")
#             go_home(drone, grid)
#             return False

#     # تم التسليم
#     drone.set_status(DroneStatus.DELIVERING)
#     print("Package delivered")

#     # الرجوع
#     go_home(drone, grid)

#     return True


# # الرجوع لنقطة البداية
# def go_home(drone, grid):

#     home_path = find_path(drone.position, (0, 0), grid)

#     # لو مفيش طريق
#     if not home_path:
#         print("Can't return home")
#         return

#     for step in home_path:
#         drone.position = step
#         drone.consume_battery(1)  # كل خطوه تقلل البطاريه اثناء الرجوع

#         print(f"Returning home: {step} | Battery: {drone.battery:.1f}%")

#     # بعد الرجوع
#     drone.set_status(DroneStatus.IDLE)

#     print("Drone returned home safely")