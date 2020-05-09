<template>
  <div>
    Output:
    <code>
      {{ $store.state.output }}
    </code>
    <br />
    <b-button @click="fetchResults">Reload</b-button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { Action } from "vuex-class";

@Component
export default class OutputComp extends Vue {
  @Action("fetchResults") fetchResults;

  created() {
    this.fetchResults();
  }
}
</script>
