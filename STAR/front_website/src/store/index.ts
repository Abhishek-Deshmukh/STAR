import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    values: {},
    fields: {}
  },
  mutations: {},
  actions: {
    async fetchParams({ state }) {
      const response = await axios.get("http://localhost:5000/params");
      state.fields = response.data;
      console.log(state.fields);
      console.log(response);
    },
    async sendRunCommand({ state }) {
      const values = state.values;
      console.log({ ...values });
      const response = await axios.post("http://localhost:5000", values);
      console.log(response);
    }
  },
  modules: {}
});
