class NonRelRouter:
    """
    A router to control if database should use
    primary database or non-relational one.
    """

    nonrel_models = {'comment'}

    def db_for_read(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return 'nonrel'
        return 'default'

    def db_for_write(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return 'nonrel'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **_hints):
        if obj1._meta.model_name in self.nonrel_models or obj2._meta.model_name in self.nonrel_models:
            return True
        return None

    def allow_migrate(self, _db, _app_label, model_name=None, **_hints):
        if _db == 'nonrel' or model_name in self.nonrel_models:
            return False
        return True
