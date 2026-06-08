import unittest

from env import BuildingRoomEnv


class BuildingRoomEnvTest(unittest.TestCase):
    def test_winning_path(self) -> None:
        env = BuildingRoomEnv()
        env.reset()

        actions = [
            "go corridor",
            "go storage",
            "take meeting_key",
            "open meeting_room",
            "go meeting_room",
            "take file",
        ]
        for action in actions:
            result = env.step(action)

        self.assertTrue(result.success)
        self.assertTrue(env.success)
        self.assertTrue(env.done)
        self.assertIn("file", env.inventory)

    def test_locked_meeting_room_blocks_entry(self) -> None:
        env = BuildingRoomEnv()
        env.reset()
        env.step("go corridor")
        env.step("go storage")

        result = env.step("go meeting_room")

        self.assertFalse(result.is_valid_action)
        self.assertIn("locked", result.observation)
        self.assertEqual(env.current_room, "storage")

    def test_invalid_movement_is_rejected(self) -> None:
        env = BuildingRoomEnv()
        env.reset()

        result = env.step("go office")

        self.assertFalse(result.is_valid_action)
        self.assertEqual(env.current_room, "entrance")
        self.assertEqual(env.invalid_action_count, 1)

    def test_key_required_to_unlock_meeting_room(self) -> None:
        env = BuildingRoomEnv()
        env.reset()
        env.step("go corridor")
        env.step("go storage")

        result = env.step("open meeting_room")

        self.assertFalse(result.is_valid_action)
        self.assertIn("need a key", result.observation)
        self.assertIn("meeting_room", env.locked_rooms)


if __name__ == "__main__":
    unittest.main()
