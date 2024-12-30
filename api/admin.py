from django.contrib import admin
from .models import Event, ChurchLeader, Attendance, Notice, Inventory, Group, GMember
from members.models import Member

admin.site.register(Event)


class MemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(Member, MemberAdmin)

class ChurchLeaderAdmin(admin.ModelAdmin):
    pass
admin.site.register(ChurchLeader, ChurchLeaderAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class InventoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Inventory, InventoryAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

class GroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(Group, GroupAdmin)

class GMemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(GMember, GMemberAdmin)