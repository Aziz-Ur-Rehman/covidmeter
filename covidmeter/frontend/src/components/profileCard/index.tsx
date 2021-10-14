import React, { FC, memo } from "react";
import Avatar from "@mui/material/Avatar";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import { API_BASE_URL } from "../../config";

interface ProfileCardProps {
  user: any;
}

const ProfileCard: FC<ProfileCardProps> = ({ user }) => {
  return (
    <Card
      sx={{
        minWidth: "100%",
        WebkitBoxShadow: "none",
        boxShadow: "none",
        height: "100%",
        textAlign: "center",
      }}
    >
      <CardContent sx={{ textAlign: "left" }}>
        <Typography gutterBottom variant="h5" component="div">
          {`Hello, ${user.first_name} ${user.last_name}!`}
        </Typography>
      </CardContent>
      <Avatar
        sx={{ width: 250, height: 250, margin: "auto" }}
        alt=""
        variant="rounded"
        src={
          user && user.profile_picture
            ? `${API_BASE_URL}${user.profile_picture}`
            : ""
        }
      />
    </Card>
  );
};

export default memo(ProfileCard);
