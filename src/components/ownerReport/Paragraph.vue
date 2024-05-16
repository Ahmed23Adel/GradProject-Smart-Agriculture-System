<script lang="ts" setup>

defineProps(["title", "paragraph"]);
</script>

<template>
  <div class="paragraph-wraper">
    <main>
      <div class="paragraph-container">
        <h5>{{ title }}</h5>
        
        <p>{{ paragraph }}</p>
      </div>
    </main>
  </div>
</template>

<style scoped>
.paragraph-wraper{
    display: flex;
    flex-direction: column;
}
main {
  margin-block: 4px;
}
.paragraph-container {
  display: flex;
  flex-direction: column;
}
h5{
    color: var(--secondary)
}
</style>
