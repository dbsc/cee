import styles from './styles.module.scss'
import { FaGoogle } from 'react-icons/fa'
import { FiX } from 'react-icons/fi'
import { signOut, signIn, useSession } from 'next-auth/client'

export function SignInButton() {
	const [session] = useSession()
	const isLogged = false

	return session ? (
		<button type="button" className={styles.signInButton} onClick={() => signOut()}>
			<FaGoogle color="#a8a8b3" />
			{session.user.name}
			<FiX className={styles.closeIcon} />
		</button>
	) : (
		<button
			type="button"
			className={styles.signInButton}
			onClick={() => signIn('google', { callbackUrl: 'http://localhost:3000/dashboard' })}
		>
			<FaGoogle color="#000" />
			Login com Google
		</button>
	)
}
