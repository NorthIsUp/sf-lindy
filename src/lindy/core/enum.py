from __future__ import absolute_import

# External Libraries
from enum import Enum


class DjangoEnum(Enum):
    @classmethod
    def as_choices(cls):
        return cls.__members__.items()


class lead_follow(DjangoEnum):
    # or get out of the way
    leader = 'Leader'
    follower = 'Follower'
