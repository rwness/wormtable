from __future__ import print_function
from __future__ import division 
import unittest
import random

import test.coretests as coretests

def main():
    # make random tests reproducable
    random.seed(3)
    testloader = unittest.TestLoader()
    #suite = testloader.loadTestsFromTestCase(coretests.TestDatabaseIntegerIntegrity)
    suite = testloader.loadTestsFromModule(coretests) 
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
