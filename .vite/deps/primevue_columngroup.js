import {
  script
} from "./chunk-RWWOPRVI.js";
import "./chunk-32WPC2CU.js";
import "./chunk-MFPFJT5E.js";
import "./chunk-LNEMQRCO.js";

// node_modules/primevue/columngroup/style/columngroupstyle.esm.js
var ColumnGroupStyle = {};

// node_modules/primevue/columngroup/columngroup.esm.js
var script$1 = {
  name: "BaseColumnGroup",
  "extends": script,
  props: {
    type: {
      type: String,
      "default": null
    }
  },
  style: ColumnGroupStyle,
  provide: function provide() {
    return {
      $parentInstance: this
    };
  }
};
var script2 = {
  name: "ColumnGroup",
  "extends": script$1,
  inheritAttrs: false,
  inject: ["$columnGroups"],
  mounted: function mounted() {
    var _this$$columnGroups;
    (_this$$columnGroups = this.$columnGroups) === null || _this$$columnGroups === void 0 || _this$$columnGroups.add(this.$);
  },
  unmounted: function unmounted() {
    var _this$$columnGroups2;
    (_this$$columnGroups2 = this.$columnGroups) === null || _this$$columnGroups2 === void 0 || _this$$columnGroups2["delete"](this.$);
  },
  render: function render() {
    return null;
  }
};
export {
  script2 as default
};
//# sourceMappingURL=primevue_columngroup.js.map
