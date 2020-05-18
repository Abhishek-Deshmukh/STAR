import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    values: {},
    fields: {},
    runInstanceData: {},
    runButtonClicked: false,
    output: ""
  },
  actions: {
    async fetchParams({ state }) {
      const response = await axios.get("http://localhost:5000/params");
      state.fields = response.data;
    },
    async sendRunCommand({ state }) {
      const values = state.values;
      const response = await axios.post("http://localhost:5000/", values);
      state.runInstanceData = response.data;
      state.runButtonClicked = true;
    },
    async fetchResults({ state }) {
      const response = await axios.get(
        "http://localhost:5000/" + state.runInstanceData["task_id"]
      );
      state.output = response.data;
    }
  },
  modules: {}
});
