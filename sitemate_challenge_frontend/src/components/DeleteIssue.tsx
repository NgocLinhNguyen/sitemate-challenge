import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalCloseButton,
  useDisclosure,
  Button,
  useToast,
} from '@chakra-ui/react'

type DeleteProps = {
  id: string
  onSuccess: () => void
}

const DeleteIssue = ({id, onSuccess}: DeleteProps) => {
  const toast = useToast()
  const { isOpen, onOpen, onClose } = useDisclosure()
  const onDelete = () => {
    fetch(
      `http://localhost:8000/api/v1/issues/${id}`,
      {
        method: 'DELETE',
      },
    ).then(() => {
      toast({
        title: 'Delete issue successfully',
        status: 'success',
        isClosable: true,
      })
      onSuccess()
      onClose()
    }).catch((error) => console.log(error))
  }
  return (
    <>
      <Button size='sm' onClick={onOpen} colorScheme='red'>Delete</Button>

      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Are you sure to delete this issue?</ModalHeader>
          <ModalCloseButton />
          <ModalFooter>
            <Button colorScheme='red' mr={3} onClick={onDelete}>
              Delete
            </Button>
            <Button variant='ghost' onClick={onClose}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default DeleteIssue