from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender= MyModel)
def my_model_pre_save(sender, instance, **kwargs):
    # Custom pre-save logic
    pass

###--------------------------------------------------------------------
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, created, **kwargs):
    if created:
        # Custom post-save logic for newly created instance
        send_notification(instance)
    else:
        # Custom post-save logic for existing instance
        update_related_data(instance)
###--------------------------------------------------------------------
def pytest_configure(config):
    # Custom configuration
    pass


###--------------------------------------------------------------------
import argparse

parser = argparse.ArgumentParser()
parser.addoption("--name", action="store", dest="name", help="Specify a name")

args = parser.parse_args()

print("Hello, " + args.name + "!")

