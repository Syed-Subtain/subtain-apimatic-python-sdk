# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.models.allocation_payment import AllocationPayment
from advancedbilling.models.apply_credit_note_event_data import ApplyCreditNoteEventData
from advancedbilling.models.apply_debit_note_event_data import ApplyDebitNoteEventData
from advancedbilling.models.apply_payment_event_data import ApplyPaymentEventData
from advancedbilling.models.bank_account_payment_profile import BankAccountPaymentProfile
from advancedbilling.models.cancellation_method import CancellationMethod
from advancedbilling.models.change_invoice_collection_method_event_data import ChangeInvoiceCollectionMethodEventData
from advancedbilling.models.component_allocation_change import ComponentAllocationChange
from advancedbilling.models.compounding_strategy import CompoundingStrategy
from advancedbilling.models.create_component_price_point import CreateComponentPricePoint
from advancedbilling.models.create_ebb_component import CreateEBBComponent
from advancedbilling.models.create_metafield import CreateMetafield
from advancedbilling.models.create_metered_component import CreateMeteredComponent
from advancedbilling.models.create_on_off_component import CreateOnOffComponent
from advancedbilling.models.create_or_update_coupon import CreateOrUpdateCoupon
from advancedbilling.models.create_or_update_flat_amount_coupon import CreateOrUpdateFlatAmountCoupon
from advancedbilling.models.create_or_update_percentage_coupon import CreateOrUpdatePercentageCoupon
from advancedbilling.models.create_prepaid_component import CreatePrepaidComponent
from advancedbilling.models.create_prepaid_usage_component_price_point import CreatePrepaidUsageComponentPricePoint
from advancedbilling.models.create_quantity_based_component import CreateQuantityBasedComponent
from advancedbilling.models.create_subscription_component import CreateSubscriptionComponent
from advancedbilling.models.credit_account_balance_changed import CreditAccountBalanceChanged
from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.custom_field_value_change import CustomFieldValueChange
from advancedbilling.models.customer_error import CustomerError
from advancedbilling.models.dunning_step_reached import DunningStepReached
from advancedbilling.models.extended_interval_unit import ExtendedIntervalUnit
from advancedbilling.models.group_settings import GroupSettings
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.invoice_issued import InvoiceIssued
from advancedbilling.models.invoice_line_item_component_cost_data import InvoiceLineItemComponentCostData
from advancedbilling.models.issue_invoice_event_data import IssueInvoiceEventData
from advancedbilling.models.item_price_point_changed import ItemPricePointChanged
from advancedbilling.models.metered_usage import MeteredUsage
from advancedbilling.models.payment_collection_method import PaymentCollectionMethod
from advancedbilling.models.payment_collection_method_changed import PaymentCollectionMethodChanged
from advancedbilling.models.payment_method_apple_pay_type import PaymentMethodApplePayType
from advancedbilling.models.payment_method_bank_account_type import PaymentMethodBankAccountType
from advancedbilling.models.payment_method_credit_card_type import PaymentMethodCreditCardType
from advancedbilling.models.payment_method_external_type import PaymentMethodExternalType
from advancedbilling.models.payment_method_paypal_type import PaymentMethodPaypalType
from advancedbilling.models.payment_related_events import PaymentRelatedEvents
from advancedbilling.models.pending_cancellation_change import PendingCancellationChange
from advancedbilling.models.prepaid_subscription_balance_changed import PrepaidSubscriptionBalanceChanged
from advancedbilling.models.prepaid_usage import PrepaidUsage
from advancedbilling.models.prepayment_account_balance_changed import PrepaymentAccountBalanceChanged
from advancedbilling.models.price_point_type import PricePointType
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.proforma_invoice_issued import ProformaInvoiceIssued
from advancedbilling.models.refund_consolidated_invoice import RefundConsolidatedInvoice
from advancedbilling.models.refund_invoice import RefundInvoice
from advancedbilling.models.refund_invoice_event_data import RefundInvoiceEventData
from advancedbilling.models.refund_success import RefundSuccess
from advancedbilling.models.remove_payment_event_data import RemovePaymentEventData
from advancedbilling.models.resume_options import ResumeOptions
from advancedbilling.models.snap_day import SnapDay
from advancedbilling.models.sorting_direction import SortingDirection
from advancedbilling.models.subscription_group_inlined import SubscriptionGroupInlined
from advancedbilling.models.subscription_group_signup_failure import SubscriptionGroupSignupFailure
from advancedbilling.models.subscription_group_signup_success import SubscriptionGroupSignupSuccess
from advancedbilling.models.subscription_product_change import SubscriptionProductChange
from advancedbilling.models.subscription_state_change import SubscriptionStateChange
from advancedbilling.models.update_metafield import UpdateMetafield
from advancedbilling.models.void_invoice_event_data import VoidInvoiceEventData
from advancedbilling.models.void_invoice_event_data_1 import VoidInvoiceEventData1
from apimatic_core.types.union_types.any_of import AnyOf
from apimatic_core.types.union_types.leaf_type import LeafType
from apimatic_core.types.union_types.one_of import OneOf
from apimatic_core.types.union_types.union_type_context import UnionTypeContext as Context


class UnionTypeLookUp:

    """The `UnionTypeLookUp` class serves as a utility class for 
    storing and managing type combinator templates.It acts as a container for the templates 
    used in handling various data types within the application.

    """
    _templates = {
        'UpdateCouponBody': OneOf(
            [
                LeafType(CreateOrUpdateCoupon)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateCouponBody': OneOf(
            [
                LeafType(CreateOrUpdateCoupon)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateComponentBody': OneOf(
            [
                LeafType(CreateMeteredComponent),
                LeafType(CreateQuantityBasedComponent),
                LeafType(CreateOnOffComponent),
                LeafType(CreatePrepaidComponent),
                LeafType(CreateEBBComponent)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ListAllComponentPricePointsInputDirection': OneOf(
            [
                LeafType(SortingDirection)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ListCustomersInputDirection': OneOf(
            [
                LeafType(SortingDirection)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ListMetadataInputDirection': OneOf(
            [
                LeafType(SortingDirection)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ListMetafieldsInputDirection': OneOf(
            [
                LeafType(SortingDirection)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ReadMrrMovementsInputDirection': OneOf(
            [
                LeafType(SortingDirection)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ListAllProductPricePointsInputDirection': OneOf(
            [
                LeafType(SortingDirection)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ListSubscriptionsInputDirection': OneOf(
            [
                LeafType(SortingDirection)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ListSubscriptionComponentsInputDirection': OneOf(
            [
                LeafType(SortingDirection)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ListSubscriptionComponentsForSiteInputDirection': OneOf(
            [
                LeafType(SortingDirection)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ProductExpirationIntervalUnitCase0': OneOf(
            [
                LeafType(ExtendedIntervalUnit)
            ]
        ),
        'ProductExpirationIntervalUnit': OneOf(
            [
                OneOf(
                    [
                        LeafType(ExtendedIntervalUnit)
                    ]
                )
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'ProductIntervalUnit': OneOf(
            [
                LeafType(IntervalUnit)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ProductTrialIntervalUnitCase0': OneOf(
            [
                LeafType(IntervalUnit)
            ]
        ),
        'ProductTrialIntervalUnit': OneOf(
            [
                OneOf(
                    [
                        LeafType(IntervalUnit)
                    ]
                )
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'SubscriptionCancellationMethod': OneOf(
            [
                LeafType(CancellationMethod)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'SubscriptionPaymentCollectionMethod': OneOf(
            [
                LeafType(PaymentCollectionMethod)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'SubscriptionGroup2': OneOf(
            [
                LeafType(SubscriptionGroupInlined)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'CustomerErrorResponseErrors': OneOf(
            [
                LeafType(CustomerError),
                LeafType(str,
                         Context.create(
                             is_array=True
                         ))
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateMetafieldsRequestMetafields': AnyOf(
            [
                LeafType(CreateMetafield),
                LeafType(CreateMetafield,
                         Context.create(
                             is_array=True
                         ))
            ]
        ),
        'MetafieldEnum': OneOf(
            [
                LeafType(str,
                         Context.create(
                             is_array=True
                         ))
            ],
            Context.create(
               is_array=True,
               is_optional=True,
               is_nullable=True
            )
        ),
        'CouponCompoundingStrategyCase0': OneOf(
            [
                LeafType(CompoundingStrategy)
            ]
        ),
        'CouponCompoundingStrategy': AnyOf(
            [
                OneOf(
                    [
                        LeafType(CompoundingStrategy)
                    ]
                )
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateOrUpdateCouponCoupon': OneOf(
            [
                LeafType(CreateOrUpdatePercentageCoupon),
                LeafType(CreateOrUpdateFlatAmountCoupon)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateOrUpdatePercentageCouponPercentage': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ]
        ),
        'CreateOrUpdatePercentageCouponCompoundingStrategy': OneOf(
            [
                LeafType(CompoundingStrategy)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'EventEventSpecificData': OneOf(
            [
                LeafType(SubscriptionProductChange),
                LeafType(SubscriptionStateChange),
                LeafType(PaymentRelatedEvents),
                LeafType(RefundSuccess),
                LeafType(ComponentAllocationChange),
                LeafType(MeteredUsage),
                LeafType(PrepaidUsage),
                LeafType(DunningStepReached),
                LeafType(InvoiceIssued),
                LeafType(PendingCancellationChange),
                LeafType(PrepaidSubscriptionBalanceChanged),
                LeafType(ProformaInvoiceIssued),
                LeafType(SubscriptionGroupSignupSuccess),
                LeafType(SubscriptionGroupSignupFailure),
                LeafType(CreditAccountBalanceChanged),
                LeafType(PrepaymentAccountBalanceChanged),
                LeafType(PaymentCollectionMethodChanged),
                LeafType(ItemPricePointChanged),
                LeafType(CustomFieldValueChange)
            ],
            Context.create(
               is_nullable=True
            )
        ),
        'UpdateMetafieldsRequestMetafields': AnyOf(
            [
                LeafType(UpdateMetafield),
                LeafType(UpdateMetafield,
                         Context.create(
                             is_array=True
                         ))
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateOrUpdateFlatAmountCouponCompoundingStrategy': OneOf(
            [
                LeafType(CompoundingStrategy)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PriceStartingQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'PriceEndingQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'PriceUnitPrice': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ]
        ),
        'ComponentCustomPricePricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupCreditCardFullNumber': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupCreditCardExpirationMonth': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupCreditCardExpirationYear': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupSignupComponentComponentId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupSignupComponentAllocatedQuantity': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupSignupComponentUnitBalance': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupSignupComponentPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'MeteredComponentPricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ]
        ),
        'MeteredComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupComponentCustomPricePricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomPriceUsedForSubscriptionCreateUpdatePriceInCents': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomPriceUsedForSubscriptionCreateUpdateInterval': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomPriceUsedForSubscriptionCreateUpdateIntervalUnit': OneOf(
            [
                LeafType(IntervalUnit)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomPriceUsedForSubscriptionCreateUpdateTrialPriceInCents': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomPriceUsedForSubscriptionCreateUpdateTrialInterval': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomPriceUsedForSubscriptionCreateUpdateTrialIntervalUnit': OneOf(
            [
                LeafType(IntervalUnit)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomPriceUsedForSubscriptionCreateUpdateInitialChargeInCents': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomPriceUsedForSubscriptionCreateUpdateExpirationInterval': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomPriceUsedForSubscriptionCreateUpdateExpirationIntervalUnit': OneOf(
            [
                LeafType(IntervalUnit)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CalendarBillingSnapDay': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'QuantityBasedComponentPricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ]
        ),
        'QuantityBasedComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'OnOffComponentPricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ]
        ),
        'OnOffComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PricePointExpirationIntervalUnit': OneOf(
            [
                LeafType(IntervalUnit)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateComponentPricePointsRequestPricePoints': AnyOf(
            [
                LeafType(CreateComponentPricePoint),
                LeafType(CreatePrepaidUsageComponentPricePoint)
            ],
            Context.create(
               is_array=True
            )
        ),
        'CreatePaymentProfileExpirationMonth': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreatePaymentProfileExpirationYear': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PrepaidUsageComponentPricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PrepaidUsageComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PrepaidUsageComponentExpirationIntervalUnit': OneOf(
            [
                LeafType(IntervalUnit)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'OveragePricingPricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ]
        ),
        'EBBComponentPricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ]
        ),
        'EBBComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateComponentPricePointRequestPricePoint': AnyOf(
            [
                LeafType(CreateComponentPricePoint),
                LeafType(CreatePrepaidUsageComponentPricePoint)
            ]
        ),
        'CreatePrepaidUsageComponentPricePointExpirationIntervalUnit': OneOf(
            [
                LeafType(IntervalUnit)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'RefundConsolidatedInvoiceSegmentUids': OneOf(
            [
                LeafType(str,
                         Context.create(
                             is_array=True
                         )),
                LeafType(str)
            ]
        ),
        'InvoiceLineItemComponentCostData2': OneOf(
            [
                LeafType(InvoiceLineItemComponentCostData)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'ComponentCostDataPricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ReadPaymentProfileResponsePaymentProfile': OneOf(
            [
                LeafType(BankAccountPaymentProfile),
                LeafType(CreditCardPaymentProfile)
            ]
        ),
        'RefundSegmentUids': OneOf(
            [
                LeafType(str,
                         Context.create(
                             is_array=True
                         )),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'RefundInvoiceRequestRefund': AnyOf(
            [
                LeafType(RefundInvoice),
                LeafType(RefundConsolidatedInvoice)
            ]
        ),
        'ApplyPaymentEventDataPaymentMethod': OneOf(
            [
                LeafType(PaymentMethodApplePayType),
                LeafType(PaymentMethodBankAccountType),
                LeafType(PaymentMethodCreditCardType),
                LeafType(PaymentMethodExternalType),
                LeafType(PaymentMethodPaypalType)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateMultiInvoicePaymentAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ]
        ),
        'RemovePaymentEventDataPaymentMethod': OneOf(
            [
                LeafType(PaymentMethodApplePayType),
                LeafType(PaymentMethodBankAccountType),
                LeafType(PaymentMethodCreditCardType),
                LeafType(PaymentMethodExternalType),
                LeafType(PaymentMethodPaypalType)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoicePaymentAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'InvoiceEventEventData': AnyOf(
            [
                LeafType(ApplyCreditNoteEventData),
                LeafType(ApplyDebitNoteEventData),
                LeafType(ApplyPaymentEventData),
                LeafType(ChangeInvoiceCollectionMethodEventData),
                LeafType(IssueInvoiceEventData),
                LeafType(RefundInvoiceEventData),
                LeafType(RemovePaymentEventData),
                LeafType(VoidInvoiceEventData),
                LeafType(VoidInvoiceEventData1)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'InvoiceEvent1PaymentMethod': OneOf(
            [
                LeafType(PaymentMethodApplePayType),
                LeafType(PaymentMethodBankAccountType),
                LeafType(PaymentMethodCreditCardType),
                LeafType(PaymentMethodExternalType),
                LeafType(PaymentMethodPaypalType)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UsageQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSubscriptionComponentComponentId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSubscriptionComponentPricePointId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionComponentPricePointType': OneOf(
            [
                LeafType(PricePointType)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ComponentSPricePointAssignmentPricePoint': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateAllocationPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'AllocationPayment2': OneOf(
            [
                LeafType(AllocationPayment)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'CreateSubscriptionComponents': OneOf(
            [
                LeafType(CreateSubscriptionComponent)
            ],
            Context.create(
               is_array=True,
               is_optional=True
            )
        ),
        'CreateSubscriptionGroup2': OneOf(
            [
                LeafType(GroupSettings),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSubscriptionOfferId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PaymentProfileAttributesExpirationMonth': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PaymentProfileAttributesExpirationYear': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ReactivateSubscriptionRequestResume': OneOf(
            [
                LeafType(bool),
                LeafType(ResumeOptions)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemQuantity': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemUnitPrice': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemProductId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemComponentId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemProductPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'RenewalPreviewComponentComponentId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'RenewalPreviewComponentPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceCouponPercentage': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceCouponAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceCouponProductFamilyId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceCouponCompoundingStrategy': OneOf(
            [
                LeafType(CompoundingStrategy)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'DeductServiceCreditAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ]
        ),
        'UpdateSubscriptionSnapDay': OneOf(
            [
                LeafType(SnapDay),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UpdateSubscriptionNetTerms': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'IssueServiceCreditAmount': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ]
        ),
        'AddSubscriptionToAGroupGroup': OneOf(
            [
                LeafType(GroupSettings),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSubscriptionGroupSubscriptionId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ]
        ),
        'CreateOrUpdateSegmentPriceUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ]
        ),
        'SegmentSegmentProperty1Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SegmentSegmentProperty2Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SegmentSegmentProperty3Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SegmentSegmentProperty4Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSegmentSegmentProperty1Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSegmentSegmentProperty2Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSegmentSegmentProperty3Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSegmentSegmentProperty4Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'RefundPrepaymentAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ]
        )
    }

    @staticmethod
    def get(name):
        return UnionTypeLookUp._templates[name]

