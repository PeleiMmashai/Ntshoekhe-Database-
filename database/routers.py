class node1Router:
  """
  A router to route app models to their respective databases.
  """
class QuthingRouter:
    """
    A router to control database operations for the 'quthing_db' database.
    """

    def db_for_read(self, model, **hints):
       
        if model._meta.app_label == 'node1':
            return 'node1_db'
        return None

    def db_for_write(self, model, **hints):
        
        if model._meta.app_label == 'node1':
            return 'node1_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        
        if obj1._meta.app_label == 'node1' and obj2._meta.app_label == 'node1':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'quthing_db' database is not used for migrations.
        """
        if app_label == 'node1':
            return db == 'node1_db'
        return None


class node2Router:
    

    def db_for_read(self, model, **hints):
        
        if model._meta.app_label == 'node2':
            return 'node2_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write 'node2_db' models go to 'node2_db' database.
        """
        if model._meta.app_label == 'node2':
            return 'node2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the 'node2_db' database.
        """
        if obj1._meta.app_label == 'node2' and obj2._meta.app_label == 'node2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'node2_db' database is not used for migrations.
        """
        if app_label == 'node2':
            return db == 'node2'
        return None


class node3Router:
    """
    A router to control database operations for the 'node3_db' database.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read 'node3_db' models go to 'node3_db' database.
        """
        if model._meta.app_label == 'node3':
            return 'node3_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write 'node3_db' models go to 'node3_db' database.
        """
        if model._meta.app_label == 'node3':
            return 'node3_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the 'node3_db' database.
        """
        if obj1._meta.app_label == 'node3' and obj2._meta.app_label == 'node3':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'node3_db' database is not used for migrations.
        """
        if app_label == 'node3':
            return db == 'node3_db'
        return None
