<script lang="ts" setup>
import {  ref } from "vue";
defineProps(["title", "imageid", "paragraph"]);
function transform(url:string){
  url=url.replace("$export=download", "");
  url=url.replace("/uc?", "/thumbnail?");
  return url
}
</script>

<template>
  <div class="paragraph-wraper">
    <main>
      <div class="paragraph-container">
        <h5>{{ title }}</h5>
      <p>{{ paragraph }}</p>
      </div>
      <img :src="transform(imageid)" alt="" />
    </main>
  </div>
</template>

<style scoped>
.paragraph-wraper{
    display: flex;
    flex-direction: column;
    
}
main {
  display: grid;
  grid-template-columns: 2fr 1fr;
  margin-block: 4px;
}
.paragraph-container {
  display: flex;
  flex-direction: column;
}
img {
  width: 90%;
  aspect-ratio: 1/0.8;
  display: inline-block;
  margin-inline: auto;
  border-radius: 8px;
}
h5{
    color: var(--secondary)
}
</style>
