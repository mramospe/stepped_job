'''
Test functions for the "core" module.
'''

__author__  = ['Miguel Ramos Pernas']
__email__   = ['miguel.ramos.pernas@cern.ch']

# Local
import stepped_job


def test_job_manager():
    '''
    Tests for the JobManager instance
    '''
    # Test singleton behaviour
    assert stepped_job.JobManager() is stepped_job.JobManager()


def test_manager():
    '''
    Test the function to get the job manager.
    '''
    # Test the function "manager"
    assert stepped_job.manager() is stepped_job.JobManager()
