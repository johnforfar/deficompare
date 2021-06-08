import React, {useCallback, useState} from "react";

type HookProps = {
  currentButton:string
};

const useActiveButton = (props:HookProps) => {
  const [activeButton, setActiveButton] = useState(props.currentButton);
    const handleButtonSelect = useCallback((selectedButton) => {
    setActiveButton(selectedButton);
  }, []);
    return {
    activeButton,
    handleButtonSelect,
  };
};

export default useActiveButton;
