<script setup>
import { ref, onMounted } from 'vue'
import Sidebar from "../components/Sidebar.vue";
import { HttpRequester } from '@/services/ApiCaller.ts';

const username = ref('')
const password = ref('')
const confirmPassword = ref('')
const userType = ref('expert') // default to expert
const error = ref()
const successMessage = ref()
const isValid = ref(false)
const users = ref([])
function validateUsername() {
    isValid.value = username.value.length >= 5 && password.value.length >= 5 && password.value === confirmPassword.value
}

function validatePassword() {
    isValid.value = username.value.length >= 5 && password.value.length >= 5 && password.value === confirmPassword.value
}

function validatePasswordConfirmation() {
    isValid.value = username.value.length >= 5 && password.value.length >= 5 && password.value === confirmPassword.value
}

async function addUser() {
    if (isValid.value) {
        const requester = new HttpRequester('register');
        const queryParams = {
            user_name: username.value,
            password: password.value,
            type: userType.value
        };
        const requester_data = await requester.callApi("POST", queryParams);
        console.log("requester_data", queryParams)
        if (!requester_data) {
            console.log("User already exists")
            error.value = "User with username exists"
            successMessage = ""
        }
        else {
            error.value = ""
            successMessage.value = "User added successfully";
            fetchAllUsers()
        }
        console.log('User added successfully')
    } else {

        console.log('Form is invalid')
    }
}

async function fetchAllUsers() {
    const requester = new HttpRequester('users');

    try {
        const requester_data = await requester.callApi("GET");
        if (requester_data.users) {
            users.value = requester_data.users; // Set the users data to the response
        } else {
            error.value = 'Failed to fetch users'; // Set error message if request fails
        }
    } catch (error) {
        console.error('Error fetching users:', error);
        error.value = 'Failed to fetch users';
    }


}
onMounted(() => {
    fetchAllUsers();
});

</script>


<template>
    <div class="page-container">
        <Sidebar class="sidebar" :selected="4" />
        <div class="main-container">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-md-6">
                        <h2 class="text-center" style="margin-top: 20px;">Add new user</h2>
                        <div class="form-group">
                            <label for="userType">User Type:</label>
                            <select id="userType" class="form-control" v-model="userType">
                                <option value="expert">Expert</option>
                                <option value="owner">Owner</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="username">Username:</label>
                            <input type="text" id="username" class="form-control" v-model="username"
                                @input="validateUsername">
                            <span v-if="username.length < 5" class="text-danger">Username must be at least 5
                                characters</span>
                        </div>
                        <div class="form-group">
                            <label for="password">Password:</label>
                            <input type="password" id="password" class="form-control" v-model="password"
                                @input="validatePassword">
                            <span v-if="password.length < 5" class="text-danger">Password must be at least 5
                                characters</span>
                        </div>
                        <div class="form-group">
                            <label for="confirmPassword">Confirm Password:</label>
                            <input type="password" id="confirmPassword" class="form-control" v-model="confirmPassword"
                                @input="validatePasswordConfirmation">
                            <span v-if="password !== confirmPassword" class="text-danger">Passwords do not match</span>
                        </div>
                        <div class="text-center" style="margin-top: 20px;">
                            <button class="btn btn-primary" :disabled="!isValid" @click="addUser">Add User</button>
                        </div>
                        <div class="text-center">
                            <div class="text-center">
                                <span v-if="successMessage" class="text-success">{{ successMessage }}</span>
                                <span v-if="error" class="text-danger">{{ error }}</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-center">
                    <div class="col-md-8">
                        <h2 class="text-center">All userss</h2>
                        <table class="table table-striped table-bordered">
                            <thead class="thead-dark">
                                <tr>
                                    <th scope="col">Username</th>
                                    <th scope="col">Password</th>
                                    <th scope="col">Type</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="user in users" :key="user._id">
                                    <td>{{ user.user_name }}</td>
                                    <td>{{ user.password }}</td>
                                    <td>{{ user.type }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style lang="scss" scoped>
.page-container {
    background-color: var(--primary);
    display: grid;
    position: relative;
    grid-template-columns: 150px 1fr;
}


.sidebar {
    position: sticky;
    top: 0;
}

.full-width-image {
    width: 100%;
    height: 500px;
    object-fit: cover;
    border-radius: 100px;

}

.text-area-parent {
    margin-right: 50px;
}

.submit-parent {
    display: flex;
    justify-content: center;
    /* Center horizontally */
    align-items: center;
    /* Center vertically */
    margin-top: 30px;
    background-color: var(--primary);
}

.submit-button {
    border-radius: 20px;
}

.submit-sub-parent {
    background-color: var(--primary);
    border: none;
}
</style>