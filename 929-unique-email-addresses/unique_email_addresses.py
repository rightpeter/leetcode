#!/usr/bin/env python3

from typing import List


class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:

        def parse_email(email: str):
            local, domain = email.split('@')

            if '+' in local:
                local = local[:local.find('+')]
            return local.replace('.', '') + '@' + domain

        email_set = set()

        for email in emails:
            email_set.add(parse_email(email))

        return len(email_set)
