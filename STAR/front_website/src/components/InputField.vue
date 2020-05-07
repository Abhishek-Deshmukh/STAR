<template>
  <div class="row mb-3">
    <div class="col-3">
      <label :for="field.name">{{ field.name }}:</label>
    </div>
    <div class="col-9">
      <b-form-input
        v-model="$store.state.values[field.id]"
        type="number"
        :id="field.name"
      ></b-form-input>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
@Component({
  props: { field: Object }
})
export default class InputField extends Vue {}
</script>
