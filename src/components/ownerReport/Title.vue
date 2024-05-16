<script lang="ts" setup>
import { defineProps,defineEmits,ref } from "vue";

const props =  defineProps(["title"]);

</script>

<template>
  <main>
    <p>{{title}}</p>
  </main>
</template>

<style scoped>
main {
  text-align: center;
  margin-bottom: 16px;
}
p{
    border: 0px;
    font-weight: bolder;
    margin-top:32px;
    font-size: 28px;
    color: var(--accentb)
}
</style>
