"""Something about robots."""


from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move.
    """
    robot.set_wheels_speed(30)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(10)
    while robot.get_right_line_sensor() == robot.get_left_line_sensor() != 0:
        robot.sleep(0.1)
    robot.sleep(2)
    robot.done()


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    while robot.get_second_line_sensor_from_left() != 0 and robot.get_second_line_sensor_from_right() != 0:
        robot.set_wheels_speed(70)
        robot.sleep(0.01)
    while robot.get_right_line_sensor() == 0 and robot.get_left_line_sensor() == 0 or \
            robot.get_second_line_sensor_from_right() == 0 or robot.get_second_line_sensor_from_left() == 0:
        robot.set_wheels_speed(70)
        robot.sleep(0.01)
        while robot.get_third_line_sensor_from_left() == 0:
            robot.set_wheels_speed(0)
            robot.set_right_wheel_speed(70)
            robot.sleep(0.01)
        while robot.get_third_line_sensor_from_right() == 0:
            robot.set_wheels_speed(0)
            robot.set_left_wheel_speed(70)
            robot.sleep(0.01)
    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    pass


if __name__ == '__main__':
    bot = FollowerBot(start_y=534, start_x=431, starting_orientation=90)
    follow_the_line(bot)
