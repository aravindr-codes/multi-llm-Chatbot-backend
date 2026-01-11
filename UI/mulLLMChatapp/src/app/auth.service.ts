import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly storageKey = 'isLoggedIn';
  private readonly expectedUsername = 'admin';
  private readonly expectedPassword = 'password123';
  private memoryFlag = false;

  login(username: string, password: string): boolean {
    const ok = username === this.expectedUsername && password === this.expectedPassword;
    if (!ok) {
      return false;
    }

    this.setLoggedIn(true);
    return true;
  }

  logout(): void {
    this.setLoggedIn(false);
  }

  isLoggedIn(): boolean {
    const stored = this.getStoredValue();
    if (stored !== null) {
      return stored;
    }

    return this.memoryFlag;
  }

  private getStoredValue(): boolean | null {
    if (typeof window === 'undefined') {
      return null;
    }

    try {
      return window.localStorage.getItem(this.storageKey) === 'true';
    } catch {
      return null;
    }
  }

  private setLoggedIn(value: boolean): void {
    this.memoryFlag = value;

    if (typeof window === 'undefined') {
      return;
    }

    try {
      if (value) {
        window.localStorage.setItem(this.storageKey, 'true');
      } else {
        window.localStorage.removeItem(this.storageKey);
      }
    } catch {
      // Ignore storage failures and rely on memory flag.
    }
  }
}
