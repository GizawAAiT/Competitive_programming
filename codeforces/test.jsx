function omit<T extends Record<string, any>, K extends keyof T>(
    object: T,
    keysToOmit: K[]
  ): Omit<T, K> {
    return Object.fromEntries(
      Object.entries(object).filter(
        ([key]) => !keysToOmit.includes(key as K)
      )
    ) as Omit<T, K>;
  }
  
  // Usage
  
  const user = {
    name: 'John Doe',
    email: 'john@example.com',
    password: 'abcd1234',
  };
  
  const newUser = omit(user, ['password']);
  console.log(newUser); // { name: 'John Doe', email: 'john@example.com' }