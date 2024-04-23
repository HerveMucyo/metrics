import unittest
from unittest.mock import patch
from tracker import packet_loss_rate

class TestPacketLossRate(unittest.TestCase):
    @patch('tracker.ping', return_value=0.0)
    def test_packet_loss_rate_no_loss(self, mock_ping):
        # Test case when no packet loss occurs
        loss_rate = packet_loss_rate("www.igihe.com", count=10)
        self.assertEqual(loss_rate, 0.0)

    @patch('tracker.ping', side_effect=[None, None, 0.0])
    def test_packet_loss_rate_some_loss(self, mock_ping):
    # Test case when some packet loss occurs
        loss_rate = packet_loss_rate("www.igihe.com", count=3)
        self.assertEqual(loss_rate, 66.67)  # Expected packet loss rate should be 66.67, not 33.33


    @patch('tracker.ping', side_effect=[None, None, None])
    def test_packet_loss_rate_all_loss(self, mock_ping):
        # Test case when all packets are lost
        loss_rate = packet_loss_rate("www.igihe.com", count=3)
        self.assertEqual(loss_rate, 100.0)

if __name__ == '__main__':
    unittest.main()
