import Cookies from 'js-cookie';

export class UserType {
    private static instance: UserType;
    private is_owner: boolean;

    private constructor() {
        if (this.getCookie("type") === "owner") {
            this.is_owner = true;
        } else {
            this.is_owner = false;
        }
    }

    public static getInstance(): UserType {
        if (!UserType.instance) {
            UserType.instance = new UserType();
        }
        return UserType.instance;
    }

    private getCookie(key: string): string | undefined {
        return Cookies.get(key);
    }

    public getUserType(): boolean {
        return this.is_owner;
    }
}
