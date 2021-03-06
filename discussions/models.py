from django.db import models

from core.models import ActivityCollection, AbstractActivity


class DiscussionActivity(AbstractActivity):

    '''-- DiscussionActivity is the class for *Discussion*.

        :Fields:
            | **title**  -- Title of activity.
            | **instructions**   -- Instructions about this activity.
            | **lesson** -- A lesson this activity belongs to, it could be null.
            | **display_order**    -- Display order of activity.
            | **created**    -- Time of creation.
            | **modified**    -- Time of last modification.
            | **is_active**    -- Flag for activation of activity.
            | **activity_type**    -- Type of current activity.
            | **posts**    -- Associated comments/posts.
            | **permission_control**    -- Flag for permission control within an activity.
            | **is_deleted**    -- Flag for soft deletion of current activity.
            | **collection**    -- The course that this discussion activity belongs to.
            | **read_after_post**  -- Flag for whether or not the student has to post their own post in order to see others' posts.
            | **private_mode**   -- Flag for whether or not students can only see their own interaction with instructors.
        :Meta:
            | **abstract**  -- Set class to abstract
            | **permissions**   -- Object level permission control("view_activity" permission is checked when *permission_control* is set to true )

    '''
    collection = models.ForeignKey(
        ActivityCollection, blank=True, null=True, on_delete=models.SET_NULL, related_name='discussions')
    read_after_post = models.BooleanField(default=False)
    private_mode = models.BooleanField(default=False)
