/** @odoo-module **/
import { PaymentScreen } from "@point_of_sale/js/Screens/PaymentScreen/PaymentScreen";
import { patch } from "@web/core/utils/patch";

patch(PaymentScreen.prototype, "fiskaltrust_payment_screen_patch", {
  async _finalizeValidation() {
    const _super = this._super.bind(this);
    alert("_finalizeValidation");
    await _super();
  }
});