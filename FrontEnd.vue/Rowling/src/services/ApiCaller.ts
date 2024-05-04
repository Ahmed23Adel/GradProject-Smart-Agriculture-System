import axios from 'axios';
import Cookies from 'js-cookie';
import { useRouter } from 'vue-router';

export class HttpRequester{
    private endpoint;
    private bearer;
    private base_endpoint;
    private router;

    constructor(endpoint: string) {
        this.endpoint = endpoint;
        this.base_endpoint = "http://127.0.0.1:8000/";

        if (this.isUserSignedIn()){
            this.bearer = this.get_cookie('token');
        }
        else{
            this.router =useRouter()
            this.router.push('/login')
        }
        
    } 

    
    public isUserSignedIn(): boolean {
        if (this.get_cookie('token')){
            return true;
        }
        return false;
    }
    public get_cookie(key: string){
        return Cookies.get(key);
    }
    

    public async callApi(method: string, queryParams?: Record<string, any>): Promise<any> {
        try {
            // Construct the URL with query parameters if provided
            const url = new URL(this.base_endpoint + this.endpoint);
            if (queryParams) {
                // Append query parameters to the URL
                for (const [key, value] of Object.entries(queryParams)) {
                    url.searchParams.append(key, value.toString());
                }
            }
            // Make the request based on the specified method
            const config = {
                headers: {
                    Authorization: `Bearer ${this.bearer}`,
                },
            };
            let response;
            switch (method.toUpperCase()) {
                case 'GET':
                    response = await axios.get(url.toString(), config);
                    break;
                case 'PUT':
                    response = await axios.put(url.toString(), {}, config);
                    break;
                case 'DELETE':
                    response = await axios.delete(url.toString(), config);
                    break;
                case 'POST':
                    response = await axios.post(url.toString(), {}, config);
                    break;
                default:
                    console.error('Invalid HTTP method specified');
                    return false;
            }
    
            // Check if the response has data and success status
            if (response.data && response.data.success) {
                // Return the response data
                return response.data.data;
            } else {
                console.error('API response did not indicate success');
                return false;
            }
        } catch (error) {
            console.error('Error calling API:', error);
        }
    }
}