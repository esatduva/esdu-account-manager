from .models import Settings

__all__ = ['get_setting']

def get_setting( name ,default ):
	setting = Settings.objects.filter(name=name)

	if setting.exists():
		return setting[0]

	return default

