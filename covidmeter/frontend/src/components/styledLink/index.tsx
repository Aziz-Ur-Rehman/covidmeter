import React from "react";
import { Link, LinkProps } from "react-router-dom";
import styled from "styled-components";

const StyledLink = styled(Link)`
  text-decoration: none;

  &:focus,
  &:hover,
  &:visited,
  &:link,
  &:active {
    text-decoration: none;
    color: black;
  }
`;

// eslint-disable-next-line
export default (props: LinkProps) => <StyledLink {...props} />;
