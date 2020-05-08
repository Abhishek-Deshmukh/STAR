import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    values: {},
    fields: { a: "int", b: "float", c: "str" }
  },
  mutations: {},
  actions: {},
  modules: {}
});
