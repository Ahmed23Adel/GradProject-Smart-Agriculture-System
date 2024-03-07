<script setup>
import InputText from 'primevue/inputtext';
import { ref } from 'vue';

const usernameValue = ref("")
const passwordValue = ref("")
</script>
<template>
    <div class="div-background">

    </div>
    <div class="content">
        <header>
            <h1>Welcome to Rowling (Login)</h1>
            <h3>This is where all plants magic take place</h3>
        </header>

        <div class="usernamePassword-div">
            <div class="card flex justify-content-center">
                <FloatLabel>
                    <InputText id="username" v-model="usernameValue" />
                    <label for="username">Username</label>
                </FloatLabel>
            </div>

        </div>

        <div class="usernamePassword-div">
            <FloatLabel>
                <Password v-model="passwordValue" toggleMask :feedback="false" />
                <label for="password">Password</label>
            </FloatLabel>
        </div>

        <div class="button-container-2">
            <span class="mas">Submit</span>
            <button type="button" name="Hover">Submit</button>
        </div>

    </div>

</template>


<style lang="scss" scoped>
@import "../assets/scss/LoginView.scss";
</style>