from lindy.models.user import *

# # -*- coding: utf-8 -*-
#
# from __future__ import absolute_import
# from django.db import transaction
#
# # External Libraries
# from django.contrib.auth.models import (
#     AbstractUser,
#     User,
# )
# from django.db.models import (
#     DateField,
#     ForeignKey,
#     ManyToManyField,
#     Model,
#     TextField,
#     URLField,
#     IntegerField,
#     EmailField,
# )
# from django.forms import (
#     ChoiceField,
# )
# from jsonfield import JSONField
# from multiprocessing import Semaphore
# from core.django import models
# from core.django.models.base import BasicInfoModelMixin
# from lindy.core.enum import lead_follow
#
#
# class User(AbstractUser):
#     #: user's phone number
#     phone_number = TextField()  # todo: make this a proper field
#
#     #: errata for users that we need to track for one-off instances
#     extra_data = JSONField()
#
#
# class BasePersona(Model):
#     user = ForeignKey(User)
#     as_a = ChoiceField(choices=lead_follow.as_choices())
#
#     @property
#     def next_event(self):
#         """
#         :return: the next Event this user is participating in.
#         """
#         pass
#
#     @classmethod
#     def many_to_many_field(cls, **kwargs):
#         """
#         Returns:
#             ManyToManyField: To User via this class.
#         """
#         return ManyToManyField(User, through=cls, **kwargs)
#
#
# class Teacher(BasePersona):
#     """
#     A persona that teaches at events
#     """
#     # feedback (standardize feedback form?)
#     # rating? (like yelp for teachers?)
#     # analytics of most played songs?
#     events = ForeignKey(Event)
#
#
# class Attendee(BasePersona):
#     """
#     A persona that attends events
#     """
#     events = ForeignKey(Event)
#
#
# class Student(Attendee):
#     """
#     A persona that attends events
#     """
#     # calculate CLTV
#     events = ForeignKey(Event)
#
#
# class Volunteer(Attendee):
#     """
#     A persona that helps run events
#     """
#     events = ForeignKey(Event)
#
#
# class Staff(Attendee):
#     """
#     A persona that helps run events
#     """
#     events = ForeignKey(Event)
#
#
# class Performer(Attendee):
#     """
#     A persona that helps run events
#     """
#     events = ForeignKey(Event)
#
#
# class Judge(Attendee):
#     """
#     A persona that helps run events
#     """
#     events = ForeignKey(Event)
#
#
# class Organizer(Attendee):
#     """
#     A persona that helps run events
#     """
#     events = ForeignKey(Event)
#
#
# class Class(Model):
#     teachers = Teacher.many_to_many_field()
#     students = Student.many_to_many_field()
#     # level (standardize on a 0-20 system? 0-taster, 1-beginner, 10-local teacher, 20-international teacher?)
#     # topics covered as tags
#     # playlist
#     video = URLField()
#     # student comments
#
#
# class EventDay(Model):
#     """
#     single day of an event
#     """
#     date = DateField()
#     classes = ForeignKey('Class')
#     tickets = ForeignKey('Tickets')
#
#     # maybe this belongs on the event, and a schedule belongs here
#     staff = Staff.many_to_many_field()
#     volunteers = Volunteer.many_to_many_field()
#
#
# class Event(Model):
#     """
#     container for an event
#
#     an event could be:
#         - a month session of classes for a school like the 920
#         - a single night dance
#         - a weekend event like fog city or focus
#     """
#     days = ForeignKey(EventDay)
#     ticket_groups = ForeignKey('TicketGroup')
#     organizers = Organizer.many_to_many_field()
#
#     @property
#     def atendees(self):
#         """
#         :return: QuerySet of all Users in attendance at the event
#         """
#         return self.students + self.dancepass + self.teachers + self.musicians
#
#     @property
#     def teachers(self):
#         """
#         :return: QuerySet of Users teaching at the event
#         """
#         pass
#
#     @property
#     def band_members(self):
#         """
#         :return: QuerySet of Users with the band at the event
#         """
#         pass
#
#     @property
#     def students(self):
#         """
#         :return: QuerySet of all Users in attending classes a the event
#         """
#         pass
#
#     @property
#     def dancepass(self):
#         """
#         :return: QuerySet of all Users only attending the dance
#         """
#         pass
#
#
# class TicketGroup(BasicInfoModelMixin):
#     limit = IntegerField(default=0)
#
#     lock = Semaphore(1)
#
#     @property
#     def available(self):
#         return max(0, self.limit - self.ticket_set.count())
#
#     def reserve(self, id, user):
#         """
#         Reserve a ticket with a lock on checking availability
#         :return:
#         """
#         with self.lock:
#             if self.available:
#                 with transaction.atomic():
#                     return Ticket.objects.create(
#                         ticket_group=self.id,
#                         reserved_by=user,
#                     )
#
#
# class Ticket(Model):
#     # need to model day passes, event passes, class passes (per level) with leader/follower balance
#     # early bird level
#     # price
#     ticket_group = ForeignKey(TicketGroup)
#     reserved_by = ForeignKey(User)
#     reserved_for = EmailField()
