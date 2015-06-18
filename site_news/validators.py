# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.utils.translation import ugettext_lazy as _

IMAGE_VALIDATOR_MAX = 1
IMAGE_VALIDATOR_EXACT = 0
IMAGE_VALIDATOR_MIN = -1

_IMAGE_VALIDATOR_TYPE_LIMIT_DISPLAY = {
    IMAGE_VALIDATOR_MAX: _(u"menor que"),
    IMAGE_VALIDATOR_EXACT: _(u"igual a"),
    IMAGE_VALIDATOR_MIN: _(u"mayor a"),
}


class ImageValidator(object):
    def __init__(self, width=None, height=None, wh_proportions=None, validation_type=IMAGE_VALIDATOR_EXACT, allowed_types=()):
        if width and height and wh_proportions:
            raise ValueError("Cannot set width, height and proportions")
        if not (width or height or wh_proportions or allowed_types):
            raise ValueError("At least set one validation")

        # Set values
        self.check_width = None
        self.check_height = None
        self.check_proportions = None
        if width and not height and not wh_proportions:
            self.check_width = int(width)
        elif not width and height and not wh_proportions:
            self.check_height = int(height)
        elif width and height and not wh_proportions:
            self.check_width = int(width)
            self.check_height = int(height)
        elif not width and not height and wh_proportions:
            self.check_proportions = float(wh_proportions)
        if width and not height and wh_proportions:
            self.check_width = int(width)
            self.check_height = int(width / wh_proportions)
        elif not width and height and wh_proportions:
            self.check_width = int(height * wh_proportions)
            self.check_height = int(height)
        # Set comparer
        if validation_type == IMAGE_VALIDATOR_EXACT:
            self.dimension_cmp = lambda x, y: x == y
        elif validation_type == IMAGE_VALIDATOR_MAX:
            self.dimension_cmp = lambda x, y: x <= y
        elif validation_type == IMAGE_VALIDATOR_MIN:
            self.dimension_cmp = lambda x, y: x >= y
        # Set limit display prefix
        self.limit_prefix = _IMAGE_VALIDATOR_TYPE_LIMIT_DISPLAY.get(validation_type, u"")
        # Set file type
        self.check_types = [x.lower().strip(".") for x in allowed_types]

    def __call__(self, value):
        if self.check_width or self.check_height or self.check_proportions:
            w, h = get_image_dimensions(value)
            if self.check_width and not self.check_height and not self.dimension_cmp(w, self.check_width):
                raise ValidationError(_(u"La imagen debe ser {2} {0}px de ancho y es de {1}px.").format(self.check_width, w, self.limit_prefix))
            elif not self.check_width and self.check_height and not self.dimension_cmp(h, self.check_height):
                raise ValidationError(_(u"La imagen debe ser {2} {0}px de alto y es de {1}px.").format(self.check_height, h, self.limit_prefix))
            elif self.check_width and self.check_height and not (self.dimension_cmp(w, self.check_width) and self.dimension_cmp(h, self.check_height)):
                raise ValidationError(_(u"La imagen debe ser {4} {0}px x {1}px y es de {2}px x {3}px.").format(self.check_width, self.check_height, w, h, self.limit_prefix))
            elif self.check_proportions and abs((float(w) / float(h)) - self.check_proportions) > 0.01:
                raise ValidationError(_(u"Las proporciones de ancho / largo de la imagen no es correcta."))

        if self.check_types:
            ext = value.name.split(".")[-1].lower()
            if not (ext in self.check_types or ("." + ext) in self.check_types):
                raise ValidationError(_(u"La extensión de la imagen no es correcta."))
