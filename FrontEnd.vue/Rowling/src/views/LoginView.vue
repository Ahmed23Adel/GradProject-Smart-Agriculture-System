<script setup>
import InputText from 'primevue/inputtext';
import { ref } from 'vue';

const usernameValue = ref("")
const passwordValue = ref("")
const isUsernameValid = ref(true)
const isPasswordValid = ref(true)


function login() {
    if (validateInput()) {

    }
}

function validateInput() {
    const username = usernameValue.value.trim();
    const password = passwordValue.value.trim();

    if (username.length < 4) {
        isUsernameValid.value = false;
    }
    else{
        isUsernameValid.value = true;
    }
    if (password.length < 4) {
        isPasswordValid.value = false;
    }
    else{
        isPasswordValid.value = true;
    }
    if (username.length < 4 || password.length < 4) {
        return false;
    }
    return true;
}


</script>
<template>
    <div class="div-background">

    </div>
    <div class="content">
        <header>
            <h1>Welcome to Rowling (Login)</h1>
            <h3>This is where all plants magic take place</h3>
        </header>

        <div class="usernamePassword-div" id="username">
            <div class="card flex justify-content-center">
                <FloatLabel>
                    <InputText id="username" v-model="usernameValue" />
                    <label for="username">Username</label>
                </FloatLabel>
            </div>

        </div>
        <Transition>
            <div class="alert-container" v-if="!isUsernameValid" @click="isUsernameValid = true">
                <div class="alert alert-error">❌ Username must be at least 4 characters..❌</div>

            </div>
        </Transition>


        <div class="usernamePassword-div" id="password">
            <FloatLabel>
                <Password v-model="passwordValue" toggleMask :feedback="false" />
                <label for="password">Password</label>
            </FloatLabel>
        </div>

        <Transition>
            <div class="alert-container" v-if="!isPasswordValid" @click="isPasswordValid = true">
                <div class="alert alert-error">❌Password must be at least 4 characters..❌</div>

            </div>
        </Transition>


        <div class="button-container-2" @click="login" id="submit">
            <span class="mas">Submit</span>
            <button type="button" name="Hover">Submit</button>
        </div>

    </div>

</template>


<style lang="scss" scoped>
@import "../assets/scss/LoginView.scss";
</style>