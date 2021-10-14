const REGRESSIONS = {
  first_name: /^[a-zA-Z ]+$/,
  last_name: /^[a-zA-Z ]+$/,
  username: /^[0-9a-zA-Z_.-]+$/,
  // eslint-disable-next-line
  email: /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/,
  password: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,20}$/,
};

interface ValidateReturn {
  success: boolean;
  message: string;
  errors: any;
}

const validateSignUpForm = (payload: any): ValidateReturn => {
  const errors: any = {};

  let message = "";
  let isFormValid = true;

  if (
    !payload ||
    typeof payload.email !== "string" ||
    !payload.email.match(REGRESSIONS.email)
  ) {
    isFormValid = false;
    errors.email = "Invalid Email";
  }

  if (
    !payload ||
    typeof payload.first_name !== "string" ||
    !payload.first_name.match(REGRESSIONS.first_name)
  ) {
    isFormValid = false;
    errors.first_name = "Invalid Name";
  }

  if (
    !payload ||
    typeof payload.last_name !== "string" ||
    !payload.last_name.match(REGRESSIONS.last_name)
  ) {
    isFormValid = false;
    errors.last_name = "Invalid Name";
  }

  if (
    !payload ||
    typeof payload.password !== "string" ||
    !payload.password.match(REGRESSIONS.password)
  ) {
    isFormValid = false;
    errors.password = "Weak Password";
  }

  if (!payload || payload.password !== payload.confirm_password) {
    isFormValid = false;
    errors.confirm_password = "Didn't Match";
  }

  if (!isFormValid) {
    message = "Invalid data!";
  }

  return {
    success: isFormValid,
    message,
    errors,
  };
};

export default validateSignUpForm;
