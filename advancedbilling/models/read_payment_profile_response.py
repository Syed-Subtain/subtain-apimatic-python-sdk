# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ReadPaymentProfileResponse(object):

    """Implementation of the 'Read Payment Profile Response' model.

    TODO: type model description here.

    Attributes:
        payment_profile (BankAccountPaymentProfile |
            CreditCardPaymentProfile): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_profile": 'payment_profile'
    }

    def __init__(self,
                 payment_profile=None):
        """Constructor for the ReadPaymentProfileResponse class"""

        # Initialize members of the class
        self.payment_profile = payment_profile 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        payment_profile = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ReadPaymentProfileResponsePaymentProfile'), dictionary.get('payment_profile'), False) if dictionary.get('payment_profile') is not None else None
        # Return an object of this model
        return cls(payment_profile)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('ReadPaymentProfileResponsePaymentProfile').validate(dictionary.payment_profile).is_valid

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('ReadPaymentProfileResponsePaymentProfile').validate(dictionary.get('payment_profile')).is_valid
