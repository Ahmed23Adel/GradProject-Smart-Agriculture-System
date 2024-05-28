<script setup>
import InputText from 'primevue/inputtext';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { HttpRequester } from '@/services/ApiCaller.ts';
import Cookies from 'js-cookie';


const usernameValue = ref("")
const passwordValue = ref("")
const isUsernameValid = ref(true)
const isPasswordValid = ref(true)
const isCredentialValid = ref(true)
const isShowLoading = ref(false)
const router =useRouter()


onMounted(() => {
    if (get_cookie('token')){
        router.push('/summary')
    }
});


async function login() {
    if (validateInput()) {
        let is_logged = await login_db();
        if (is_logged){
            router.push('/summary')
        }
        
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


const token = ref()
const userType = ref()
async function login_db(){
    isShowLoading.value = true;
    const requester = new HttpRequester('login', true);
    const queryParams = {
        user_name: usernameValue.value,
        password: passwordValue.value.trim(),
    };
    console.log(queryParams)
    const requester_data = await requester.callApi('GET', queryParams);
    console.log("requester_data", requester_data)
    isShowLoading.value = false;
    if (! requester_data){
        console.log("Credential wrong")
        isCredentialValid.value = false;
        return false
    } 

    token.value = requester_data.token;
    userType.value = requester_data.user_type
    saveCookie('token',token.value)
    saveCookie('type',userType.value)
    return true
}

function saveCookie(key, value) {
    Cookies.set(key, value, { expires: 1 }); // Expires in 1 days
}
function is_token_valid() {
    let key="token";
    const cookieValue = Cookies.get(key); // Retrieve the cookie value
    if (cookieValue !== undefined && cookieValue !== null) { // Check if cookie exists
        const cookieExpiration = Cookies.getJSON(key + '_expires'); // Get expiration date
        if (!cookieExpiration || new Date(cookieExpiration) > new Date()) { // Check expiration
            return true; // Cookie is valid
        } else {
            // Cookie has expired
            // You can remove the expired cookie if needed
            Cookies.remove(key);
            return false; // Or handle the expiration accordingly
        }
    }
    return false; // Return null if cookie doesn't exist
}
function get_cookie(key){
    return Cookies.get(key);
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
        <div v-if="isShowLoading">
            <ProgressSpinner />
        </div>

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
                <!-- <div class="alert alert-error">❌ Username must be at least 4 characters..❌</div> -->
                <Message severity="error">Username must be at least 4 characters</Message>

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
                <!-- <div class="alert alert-error">❌Password must be at least 4 characters..❌</div> -->
                <Message severity="error">Password must be at least 4 characters</Message>

            </div>
        </Transition>
        <Transition>
            <div class="alert-container" v-if="!isCredentialValid" @click="isCredentialValid = true">
                <Message severity="error">Either username or password is not correct</Message>

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