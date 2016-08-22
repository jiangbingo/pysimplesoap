import os
from .base import BaseTestcase
from pysimplesoap.wsdl import parse


class TestWsdlParsing(BaseTestcase):
    def test_with_import(self):
        _, _, _, _, services = parse(os.path.abspath('tst/data/register.wsdl'))
        self.assertEqual(services.keys(), ['NE3SRegistrationService'])
        self.assertEqual(services['NE3SRegistrationService']['documentation'], '')
        self.assertEqual(services['NE3SRegistrationService']['ports']['ne3sRegistration']['operations']['startRegistration']['output']['startRegistrationResponse']['agentIdentity']['uniqueId'], str)
    def test_with_import_and_multiservices(self):
        _, _, _, _, services = parse(os.path.abspath('tst/data/ne3s.wsdl'))
        self.assertEqual(services['NE3SBasicNotificationsService']['documentation'], '')
        self.assertEqual(services['NE3SBasicNotificationsService']['ports']['ne3sBasicNotifications']['operations']['transferNotification']['output']['transferNotificationResponse']['managerRegistrationId'], str)
        self.assertEqual(services['NE3SBulkOperationsService']['ports']['ne3sBulkOperations']['operations']['upload']['input']['upload']['sessionId'], str)

