<script lang="ts" setup>
import { defineProps,defineEmits,ref } from "vue";

const props =  defineProps(["title"]);
const newTitle = ref('')
const emit = defineEmits(['titleChange'])
newTitle.value=props.title
</script>

<template>
  <main>
    <input type="text" @change="emit('titleChange',newTitle)" v-model="newTitle"/>
  </main>
</template>

<style scoped>
main,input {
  text-align: center;
  margin-bottom: 16px;
}
input{
    border: 0px;
    font-weight: bolder;
    margin-top:32px;
    font-size: 28px;
    color: var(--accentb)
}
</style>
